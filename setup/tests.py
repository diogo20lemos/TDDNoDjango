from django.test import LiveServerTestCase
from selenium import webdriver
from animais.models import Animal
# from time 


class AnimaisTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(
            'C:/Users/diogo/Desktop/Dev/tdd/tdd_busca_animal/chromedriver')
        self.animal = Animal.objects.create(
            nome_animal = 'leão',
            predador = 'Sim',
            venenoso = 'Não',
            domestico = 'Não'
        )

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
        buscar_animal_input = self.browser.find_element_by_css_selector('input#buscar-animal')
        self.assertEqual(buscar_animal_input.get_attribute('placeholder'),'Exemplo: leão')

        # Ele pesquisa por leão e clica no botão pesquisar
        buscar_animal_input.send_keys('leão')
        # time.sleep(2) para visualizar acontecendo 
        self.browser.find_element_by_css_selector('form button').click()


        # O site exibe 4 caracteristicas do animal pesquisado.
        caracteristicas = self.browser.find_elements_by_css_selector('.result-description')
        self.assertGreater(len(caracteristicas), 3)
        
        # Ele desiste de adotar um leão.

        