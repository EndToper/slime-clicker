from emailer import check
import pytest
def test_1():
    assert check("Email@123@lol@email.ru") == False
    assert check('Email@[lol]/ru') == False
    assert check('Email@lol/ru') == False
    assert check('Email@lol\ru') == False
    assert check('Email\n@lol.ru') == False
    assert check('Email\a@lol.ru') == False
    assert check('email@notochki') == False
    assert check('email@r.u') == False
    assert check('email@rrgr.u') == False
    assert check('email@r5533.u5e3') == False
    assert check('email@lolik.ahahaha.ru') == True
    assert check(True) == False
    assert check(['123','@','gmail']) == False
    assert check({'lol':'kek'}) == False

#не мои тесты
def test_1():
    assert check('hello@mail.ru') == True,'придумал ОГ'
    assert check('h@llo@mail.ru') == False,'придумал ОГ'
    assert check('Жhello@mail.ru') == False,'придумал ОГ'

#(By KruASe) (Вроде все стандартное...)
def test_2(): 
    assert check('')==False
    assert check(123)==False
    assert check('123')==False
    assert check('sm th@email.com')==False
    assert check('#1535@email.ru')==False
    assert check('smth@email.emaillllll')==False
    assert check('smth@email.em7')==False
    assert check('smth@.ru')==False

# Kletcka - Воронков Михаил

def test_3():     
    assert check('capybara@capy.bara') == True
    assert check('capybara@capy.ba.ra')  == True
    assert check('capybara.capy.bara') == False
    assert check('capybara@capy@bara') == False
    assert check('capybara!@capy.bara')  == False
    assert check('капибара@capy.bara')  == False
    assert check('capy bara@capy.bara')  == False
    assert check('capybara@capy')  == False
    assert check('capybara@c.apybara')  == False
    assert check('capybara@capy.ba.ra1')  == False
    assert check('capybara@ca.pybara')  == False
    assert check('capybara@capybar.a')  == False
    assert check('capybara@cap')  == False


# NuoKey - Тимофей Ганицев
def test_4():
    assert check('hello.sdf.qsdf@gmail.com') == True