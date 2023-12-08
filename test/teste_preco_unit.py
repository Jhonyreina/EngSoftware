import unittest

from scr.Funcoes import preco_unitario

class testePrecoUni(unittest.TestCase):
        
    def test_Preco_unitario(self):
        #500 gramas de um produto custa R$ 20.00, 1 grama custa R$ 0.04
        self.assertEqual(preco_unitario(20.00, 500), 0.04)

if __name__ == '__name__':
    unittest.main()