from django.test import LiveServerTestCase
from selenium import webdriver


class AnimaisTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(
            'C:/Users/diogo/Desktop/Dev/tdd/tdd_busca_animal/chromedriver')

    def tearDown(self):
        self.browser.quit()

    def test_buscando_um_novo_animal(self):
        """
        Teste se um usuário encontra um animal na pesquisando.
        """

        # Vini, deseja encontrar um novo animal para adotar

        # Ele encontra o Busca Animal e decide usar o site,
        home_page = self.browser.get(self.live_server_url + '/')
        #  porque ele vê o menu do site escrito Bucar Animal.
        brand_alement = self.browser.find_element_by_css_selector('.navbar')
        self.assertEqual('Busca Animal', brand_alement.text)
        # Ele vê um campo para pesquisar animal pelo nome.

        # O site exibe 4 caracteristicas do animal pesquisado.

        # Ele desiste de adotar um leão.

        pass