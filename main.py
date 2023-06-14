from page_dados.bot import Bot



class Roda_bot(Bot):
    def __init__(self):
        self.bot = Bot()
        self.bot.pegando_dados()





if __name__ == "__main__":
    Roda_bot()
    exit()