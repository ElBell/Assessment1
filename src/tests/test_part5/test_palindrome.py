from unittest import TestCase

from src.main.part5.palindrome import Palindrome


class TestPalindrome(TestCase):
    def test_solution0(self):
        expected = Palindrome.count_palindromes("aaa")
        actual = 6
        self.assertEqual(expected, actual)

    def test_solution1(self):
        expected = Palindrome.count_palindromes("abccba")
        actual = 9
        self.assertEqual(expected, actual)

    def test_solution2(self):
        expected = Palindrome.count_palindromes("daata")
        actual = 7
        self.assertEqual(expected, actual)

    def test_solution3(self):
        expected = Palindrome.count_palindromes("lrfkqyuqfj")
        actual = 10
        self.assertEqual(expected, actual)

    def test_solution4(self):
        expected = Palindrome.count_palindromes("kxyqvnrtys")
        actual = 10
        self.assertEqual(expected, actual)

    def test_solution5(self):
        expected = Palindrome.count_palindromes(
            "ltvzkqtpvolphckcyufdqmlglimklfzktgygdttnhcvpfdfbrpzlkvshwywshtdgmbqbkkxcvgumonmwvytbytnuqhmfjaqtgngcwkuzyamnerphfmwevhwlezohyeehbrcewjxvceziftiqtntfsrptugtiznorvonzjfeacgamayapwlmbzitzszhzkosvnknberbltlkggdgpljfisyltmmfvhybljvkypcflsaqevcijcyrgmqirzniaxakholawoydvchveigttxwpukzjfhxbrtspfttotafsngqvoijxuvqbztvaalsehzxbshnrvbykjqlrzzfmlvyoshiktodnsjjpqplciklzqrxloqxrudygjtyzleizmeainxslwhhjwslqendjvxjyghrveuvphknqtsdtwxcktmwwwsdthzmlmbhjkmouhpbqurqfxgqlojmwsomowsjvpvhznbsilhhdkbdxqgrgedpzchrgefeukmcowoeznwhpiiduxdnnlbnmyjyssbsococdzcuunkrfduvouaghhcyvmlkzaajpfpyljtyjjpyntsefxiswjutenuycpbcnmhfuqmmidmvknyxmywegmtunodvuzygvguxtrdsdfzfssmeluodjgdgzfmrazvndtaurdkugsbdpawxitivdubbqeonycaegxfjkklrfkraoheucsvpiteqrswgkaaaohxxzhqjtkqaqhkwberbpmglbjipnujywogwczlkyrdejaqufowbigrsnjniegvdvotugocedktcbbufnxorixibbdfrzuqsyrfqghoyqevcuanuujszitaoaowsxyglafbwzddoznrvjqeyqignpitruijvyllsibobjltusrypanvybsfrxtlfmpdidtyozoolzslgdgowijatklvjzscizrkupmsoxftumyxifyunxucubvkfctkqlroqgzjvjwzizppvsomflvioemycnp")
        actual = 1084
        self.assertEqual(expected, actual)
