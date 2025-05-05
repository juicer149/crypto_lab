from ciphers.scytal import ScytalCipher
import logging

# Konfigurera loggern
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%H:%M:%S"
)

def print_as_ribbon(text: str, columns: int):
    logger.info("Utdragen rämsa:")
    rows = (len(text) + columns - 1) // columns
    padded = text.ljust(rows * columns)

    for col in range(columns):
        for row in range(rows):
            index = row * columns + col
            if index < len(text):  # undvik att visa padding
                logger.info(f"| {padded[index]} |")


def print_wrapped_2d(text: str, columns: int):
    logger.info("Lindad runt stav:")
    rows = (len(text) + columns - 1) // columns
    padded = text.ljust(rows * columns)

    # Skapa tom matris
    matrix = [[' ' for _ in range(columns)] for _ in range(rows)]

    index = 0
    for col in range(columns):  # fyll kolumnvis
        for row in range(rows):
            if index < len(padded):
                matrix[row][col] = padded[index]
                index += 1

    # Skriv ut radvis med växande indrag
    for row_index, row in enumerate(matrix):
        indent = " " * row_index
        line = ''.join(f"\\{char}\\" for char in row)
        logger.info(indent + line)




def run_cli():
    logger.info("=" * 30)
    logger.info("Kryptolabb CLI")
    logger.info("=" * 30)
    while True:
        logger.info("[1] Scytal-kryptering")
        logger.info("[0] Avsluta")

        choice = input("Välj alternativ: ")
        
        if choice == "1":
            scytal_cli()
        elif choice == "0":
            logger.info("Avslutar...")
            break
        else:
            logger.warning("Ogiltigt val. Försök igen.")


def scytal_cli():
    text: str = input("Skriv meddelande att kryptera: ")
    cols: int = input("Antal kolumner (ex: 5): ")

    if not cols.isdigit():
        logger.warning("Du måste ange ett heltal.")
        return

    cols = int(cols)
    cipher = ScytalCipher(text, columns=cols)

    # Visa som utdragen rämsa i krypteringsordning (kolumnvis)
    print_as_ribbon(cipher.clean_text, cols)

    encrypted = cipher.encrypt()
    logger.info(f"Krypterat meddelande: {encrypted}")

    should_decrypt = input("Vill du dekryptera det direkt? (j/n): ").lower()
    if should_decrypt == 'j':
        decrypted = ScytalCipher(encrypted, columns=cols).decrypt()
        logger.info(f"Dekrypterat:\n{decrypted}")

        # Visa som lindad spiral i 2D
        print_wrapped_2d(decrypted, cols)

    elif should_decrypt == 'n':
        logger.info("OK, dekryptering hoppas över.")
    else:
        logger.warning("Ogiltigt svar. Inget dekryptering utfördes.")

