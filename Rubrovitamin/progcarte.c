#include <avr/io.h>
#include <stdint.h>
#include <avr/eeprom.h>
#include <avr/pgmspace.h>
#include <stdarg.h>
#include <stdbool.h>

// Définition du password administrateur
#define ADMIN_PASSWORD "admin"

// Définitions de deux booléen à l'état false qui permetteront de vérifier si le password est correct et si le password est entré correctement
bool isPasswordCorrect = false;
bool isPasswordEntered = false;

//------------------------------------------------
// Programme "hello world" pour carte à puce
// 
//------------------------------------------------


// déclaration des fonctions d'entrée/sortie définies dans "io.c"
void sendbytet0(uint8_t b);
uint8_t recbytet0(void);

// variables globales en static ram
uint8_t cla, ins, p1, p2, p3;	// entête de commande
uint8_t sw1, sw2;		// status word

int taille;		// taille des données introduites -- est initialisé à 0 avant la boucle
#define MAXI 128	// taille maxi des données lues
uint8_t data[MAXI];	// données introduites

// Procédure qui renvoie l'ATR
void atr(uint8_t n, char* hist)
{
  sendbytet0(0x3b);	// définition du protocole
  
  n = 0xF0 + n  +1 ;
  sendbytet0(n);		// nombre d'octets d'historique
  sendbytet0(0x01); //TA 
  sendbytet0(0x05); //TB
  sendbytet0(0x05); //TC 
  sendbytet0(0x00); //TD protocole t=0
  sendbytet0(0x00); //CAT 

  while(n--)		// Boucle d'envoi des octets d'historique
    {
      sendbytet0(*hist++);
    }
}


// Gestion des erreurs 
//-------------
// La gestion d'erreur est basée sur la norme ISO 7816-4

#define ERR_INVALID_SIZE  0x6C  // erreur de taille invalide
#define ERR_UNKNOWN_CLASS 0x6E  // erreur de classe invalide
#define ERR_UNKNOWN_INS   0x6D  // erreur d'instruction invalide

// Fonction de gestion des erreurs
void error(uint8_t error_code) {
    // Envoie le code d'erreur en tant que premier octet de la réponse
    sendbytet0(error_code);
    // Envoie le second octet de la réponse (informations supplémentaires sur l'erreur)
    sendbytet0(sw2);
}


// transactions
//-------------

// nombre maximal d'opérations par transaction
#define max_ope		3
// taille maximale totale des données échangées lors d'une transaction
#define max_data	64
// définition de l'état du buffer -- plein est une valeur aléatoire
typedef enum{vide=0, plein=0x1c} state_t;
// la variable buffer de transaction mémorisée en eeprom
struct
{
	state_t state;			// etat
	uint8_t nb_ope;			// nombre d'opération dans la transaction
	uint8_t taille_ope[max_ope];		// table des tailles des transferts
	uint8_t*p_dst[max_ope];		// table des adresses de destination des transferts
	uint8_t buffer[max_data];	// données à transférer
}
ee_transfert EEMEM={vide}; // l'état doit être initialisé à "vide"


// engagement d'une transaction
// appel de la forme engage(n1, p_src1, p_dst1, n2, p_src2, p_dst2, ... 0)
// ni : taille des données à transférer
// p_srci : adresse des données à transférer
// p_dsti : destination des données à transférer
void engage(int taille_ope, ...)
{
  va_list args;
	uint8_t nb_ope;
	uint8_t*p_src;
	uint8_t*p_buf;

	// mettre l'état à "vide"
  // On prend la case state et on la set à la valeur vide = 0
	eeprom_write_byte((uint8_t*)&ee_transfert.state,vide);


	va_start(args,taille_ope);
	nb_ope=0;
	p_buf=ee_transfert.buffer;
	while(taille_ope!=0)
	{
		// transférer les données dans le buffer
		p_src=va_arg(args,uint8_t*);
		eeprom_write_block(p_src,p_buf,taille_ope);
		p_buf+=taille_ope;
		// écriture de l'adresse de destination
		eeprom_write_word((uint16_t*)&ee_transfert.p_dst[nb_ope],(uint16_t)va_arg(args,uint8_t*));
		// écriture de la taille des données
		eeprom_write_byte(&ee_transfert.taille_ope[nb_ope],taille_ope);
		nb_ope++;
		taille_ope=va_arg(args,int);	// taille suivante dans la liste
	}
	// écriture du nombre de transactions
	eeprom_write_byte(&ee_transfert.nb_ope,nb_ope);
	va_end(args);
	// mettre l'état à "data"
	eeprom_write_byte((uint8_t*)&ee_transfert.state,plein);
}

// validation d'une transaction
void valide()
{
	state_t etat;		// état
	uint8_t nb_ope;		// nombre d'opérations dans la transaction
	uint8_t*p_src, *p_dst;	// pointeurs sources et destination
	uint8_t i,j;
	uint8_t taille_ope;		// taille des données à transférer

	// lecture de l'état du buffer
	etat=eeprom_read_byte((uint8_t*)&ee_transfert.state);
	// s'il y a quelque chose dans le buffer, transférer les données aux destinations
	if (etat==plein)	// un état non plein est interprété comme vide
	{
		// lecture du nombre d'opérations à valider
		nb_ope=eeprom_read_byte(&ee_transfert.nb_ope);
		p_src=ee_transfert.buffer; // src = contenu du buffer
		// boucle sur le nombre d'opérations
		for (i=0;i<nb_ope;i++)
		{
			// lecture de la taille à transférer 
			taille_ope=eeprom_read_byte(&ee_transfert.taille_ope[i]); // taille de l'opération en cours
			// lecture de la destination
			p_dst=(uint8_t*)eeprom_read_word((uint16_t*)&ee_transfert.p_dst[i]);
			// transfert eeprom -> eeprom du buffer vers la destination
			for(j=0;j<taille_ope;j++)
			{
        // pour chaque destinations et sources, on ecrit les adresses ??????????????????????????????????
				eeprom_write_byte(p_dst++,eeprom_read_byte(p_src++));
			}
		}
	}
  // a la fin des opérations, mettre l'état vide
	eeprom_write_byte((uint8_t*)&ee_transfert.state,vide);	
}



// émission de la version
// t est la taille de la chaîne sv
void version(int t, char* sv)
{
    	int i;
    	// vérification de la taille
    	if (p3!=t)
    	{
        	sw1=0x6c;	// taille incorrecte
        	sw2=t;		// taille attendue
        	return;
    	}
	sendbytet0(ins);	// acquittement
	// émission des données
	for(i=0;i<p3;i++)
    	{
        	sendbytet0(sv[i]);
    	}
    	sw1=0x90;
}

// Définition de la taille maximum du mot de passe
#define MAX_PASSWORD_LENGTH 5

// Fonction qui compare deux tableaux d'octets
int compareByteArrays(const void *a, const void *b, size_t size) {
    const uint8_t *byteArrayA = (const uint8_t *)a;
    const uint8_t *byteArrayB = (const uint8_t *)b;

    for (size_t i = 0; i < size; i++) {
        if (byteArrayA[i] != byteArrayB[i]) {
            return byteArrayA[i] - byteArrayB[i];
        }
    }

    return 0;  // Les tableaux sont identiques
}


// Fonction qui récupère l'octer qui contient la valeur du mdp entré par l'utilisateur lors de l'input envoyé par Lubiana
void get_input_py(int BUFFSIZE)
{
    char py_pwd[BUFFSIZE];
    int i;

    // contrôle p3
    if (p3 > BUFFSIZE)
    {
        sw1 = 0x6c;
        sw2 = BUFFSIZE;
        return;
    }
    // acquittement
    sendbytet0(ins);
    // traitement de la commande
    for (i = 0; i < p3; i++)
    { // lecture des données
        py_pwd[i] = recbytet0();
    }

    // Utilisation de la fonction compareByteArrays pour comparer le mdp admin et le mdp entré par l'utilisateur
    if (compareByteArrays(py_pwd, (const uint8_t *)ADMIN_PASSWORD, BUFFSIZE) != 0) {
        sw1 = 0x6a;
        isPasswordCorrect = false;  // Mot de passe incorrect
        isPasswordEntered = true;   // Mot de passe a été entré (peut être incorrect)
        return;
    }
    isPasswordCorrect = true;  // Mot de passe correct
    isPasswordEntered = true;  // Mot de passe a été entré et est correct
    sw1 = 0x90;
}


// Définition des tailles maximales pour les données personnelles et les codes PIN/PUK
#define MAX_PERSO 32 // taille max des données nom prenom num_etudiant
#define TAILLE_SOLD 8 // taille max du solde
#define TAILLE_PIN 4 // taille max du PIN
#define TAILLE_PUK 4 // taille max du PUK

// Déclaration et initialisation des variables dans l'EEPROM
uint16_t ee_taille EEMEM=0; // Initialisation des données à 0
uint16_t ee_taille2 EEMEM=32; // Ecriture du solde à partir du 32 ème bit de l'EEPROM
uint16_t ee_codePIN EEMEM=40; // Ecriture du PIN à partir du 38 bit de l'EEPROM
uint16_t ee_codePUK EEMEM=44; // Ecriture du PUK à partir du 42 bit de l'EEPROM


unsigned char ee_perso[MAX_PERSO] EEMEM; // Données stockées en EEPROM
unsigned char ee_perso2[TAILLE_SOLD] EEMEM; // Solde stocké en EEPROM
unsigned char ee_perso_PIN[TAILLE_PIN] EEMEM; // PIN ET PUK stockés en EEPROM
unsigned char ee_perso_PUK[TAILLE_PUK] EEMEM;


// Fonction intro perso qui permet d'introduire des données dans l'EEPROM
// Cette fonction est utilisé pour introduire nom, prenom, num etu, PIN, PUK.
// Cette fonction est sécurisée par un mot de passe admin
void intro_perso(int buffsize, uint16_t *taille, unsigned char *perso) {

    // On vérifie si le mdp est entré correctement
    if (!isPasswordEntered) {
        sw1 = 0x6a;  // Mot de passe non entré
        sw2 = 0x00;
        return;
    }

    char buffer[buffsize];
    int i;
    // contrôle p3
    if (p3 > buffsize) {
        sw1 = 0x6c;
        sw2 = buffsize;
        return;
    }
    // acquittement
    sendbytet0(ins);
    // traitement de la commande
    for (i = 0; i < p3; i++) { // lecture des données
        buffer[i] = recbytet0();
    }
    uint16_t pp3 = p3;
    engage(2, &pp3, taille, p3, buffer, perso, 0);


    valide();

    // recopie en eeprom
    // eeprom_write_block(buffer, perso, p3);
    // écriture de la taille
    // eeprom_write_word(taille, p3);
    
    // Mise à jour du statut word, car la fonction a réussi
    sw1 = 0x90;
}

// Meme fonction que intro perso mais non sécurisée par un mdp. Cette fonction est utilisée
// pour initialiser le solde.
void intro_perso_sans_mdp(int buffsize, uint16_t *taille, unsigned char *perso) {

    char buffer[buffsize];
    int i;
    // contrôle p3
    if (p3 > buffsize) {
        sw1 = 0x6c;
        sw2 = buffsize;
        return;
    }
    // acquittement
    sendbytet0(ins);
    // traitement de la commande
    for (i = 0; i < p3; i++) { // lecture des données
        buffer[i] = recbytet0();
    }
    uint16_t pp3 = p3;
    engage(2, &pp3, taille, p3, buffer, perso, 0);


    valide();

    // recopie en eeprom
    // eeprom_write_block(buffer, perso, p3);
    // écriture de la taille
    // eeprom_write_word(taille, p3);
    
    // Mise à jour du statut word, car la fonction a réussi
    sw1 = 0x90;
}


// Fonction lire_perso permet de lire les données de l'EEPROM comme le nom, le prenom, le num etu
// le solde et le PIN PUK
void lire_perso(uint16_t *perso, unsigned char *test)
{
  int i;
  char buffer[MAX_PERSO];
  uint8_t taille;
  taille = eeprom_read_byte(perso);
  if (p3 != taille)
  {
    sw1 = 0x6c;
    sw2 = taille;
    return;
  }
  sendbytet0(ins);
  eeprom_read_block(buffer, test, taille);
  for (i = 0; i < p3; i++)
  {
    sendbytet0(buffer[i]);
  }
  sw1 = 0x90;
}

// Fonction delete_data permet de mettre les valeurs des 40 premiers bits à 0 
// soit elle permet de delete les datas et le solde de l'EEPROM
void delete_data(unsigned char *perso, uint16_t *taille)
{

  if (!isPasswordEntered) {
        sw1 = 0x6a;  // Mot de passe non entré
        sw2 = 0x00;
        return;
  }

  uint16_t zeros = 0;
  *taille = eeprom_read_byte(perso);

  if (p3 != *taille)
  {
    sw1 = 0x6c;
    sw2 = *taille;
    return;
  }
  
  engage(1, zeros, taille, p3, zeros, perso, 0);
  valide();
  // écriture de la taille
	// eeprom_write_word(taille, zeros);
	// status word
	// recopie en eeprom
	// eeprom_write_block(0, perso, p3);



	sw1=0x90;
}

  // Programme principal
//--------------------
int main(void)
{
  // initialisation des ports
	ACSR=0x80;
	PORTB=0xff;
	DDRB=0xff;
	DDRC=0xff;
	DDRD=0;
	PORTC=0xff;
	PORTD=0xff;
	ASSR=(1<<EXCLK)+(1<<AS2);
	//TCCR2A=0;
  //	ASSR|=1<<AS2;
	PRR=0x87;


	// ATR
  atr(11,"Hello scard");

	taille=0;
	sw2=0;		// pour éviter de le répéter dans toutes les commandes
  // boucle de traitement des commandes
 for(;;)
  	{
      // lecture de l'entête
      cla=recbytet0();
      ins=recbytet0();
      p1=recbytet0();
      p2=recbytet0();
      p3=recbytet0();
      sw2=0;
      switch (cla) {
    case 0x80:
        switch (ins) {
            case 0:
                version(4, "1.00");
                break;

            case 1:
                get_input_py(MAX_PASSWORD_LENGTH);
                break;

            case 3:
                if (isPasswordCorrect) {
                  intro_perso(MAX_PERSO, &ee_taille, ee_perso);
                } else {
                // Le mot de passe est incorrect, gestion des erreurs ici si nécessaire
                    sw1 = 0x6A;  // SW1 pour erreur d'authentification
                    sw2 = 0x00; 
                }
                break;


            case 4:
                lire_perso(&ee_taille, ee_perso);
                break;

            case 7:
                lire_perso(&ee_taille2, ee_perso2);
                break;

            case 8:
                intro_perso_sans_mdp(TAILLE_SOLD, &ee_taille2, ee_perso2);
                break;

            case 5:
                if (isPasswordCorrect) {
                    delete_data(ee_perso, &ee_taille);
                } else {
                    sw1 = 0x6A;  // SW1 pour erreur d'authentification
                    sw2 = 0x00; 
                }
                break;

            case 6:
                if (isPasswordCorrect) {
                    intro_perso(TAILLE_PIN, &ee_codePIN, ee_perso_PIN);
                } else {
                    sw1 = 0x6A;  // SW1 pour erreur d'authentification
                    sw2 = 0x00; 
                }
                break;

            case 9:
                if (isPasswordCorrect) {
                    intro_perso(TAILLE_PUK, &ee_codePUK, ee_perso_PUK);
                } else {
                    sw1 = 0x6A;  // SW1 pour erreur d'authentification
                    sw2 = 0x00; 
                }
                break;

            default:
                error(ERR_UNKNOWN_INS); // code erreur ins inconnu
        }
        break;

    case 0x81: // Nouvelle classe
        switch (ins) {
            // Ajoutez ici le traitement des instructions pour la classe 0x81
            // case ... :
            //     // Traitement pour l'instruction spécifique

            case 0:
                lire_perso(&ee_codePUK, ee_perso_PUK);
                break;
            
            case 1:
                lire_perso(&ee_codePIN, ee_perso_PIN);
                break;

            default:
                error(ERR_UNKNOWN_INS); // code erreur ins inconnu pour la classe 0x81
        }
        break;

    default:
        error(ERR_UNKNOWN_CLASS); // code erreur classe inconnue
}

sendbytet0(sw1); // envoi du status word
sendbytet0(sw2);

  	}
  	return 0;
}

//}