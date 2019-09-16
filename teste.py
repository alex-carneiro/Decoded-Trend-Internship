import os
from gabarito import decoded_numbers,\
                           decoded_strings,\
                           decoded_file,\
                           decoded_json,\
                           decoded_web

def teste_decoded_numbers():
    assert decoded_numbers(1)   == 1
    assert decoded_numbers(2) == 2/3
    assert decoded_numbers(3) == 3/5
    assert decoded_numbers(4) == 4/7
    assert decoded_numbers(5) == 5/9
    assert decoded_numbers(6) == 6/11
    assert decoded_numbers(0) is None
    assert decoded_numbers(-1) is None
    assert decoded_numbers(1.5) is None

def teste_decoded_strings():
    assert decoded_strings("ABC XYZ") == "abc_xyz"
    assert decoded_strings("??123 é isso aí!") == "123_e_isso_ai"
    assert decoded_strings("um, dois, três") == "um_dois_tres"
    assert decoded_strings("C@beça na média") == "c_beca_na_media"
    assert decoded_strings("***(!%!$@)") == ""

def teste_decoded_file():
    assert decoded_file(os.path.join('files', 'file.txt')) == (['abc', 'a1s'],
                                                               ['xyz', 's1a'],
                                                               ['123', '1as'],
                                                               ['@bc'])

def teste_decoded_json():
    assert decoded_json(os.path.join('files', 'file.json')) == {"n0": 1,
                                                                "n1": 17,
                                                                "n2": 38,
                                                                "n3": 56,
                                                                "n4": 314}

def teste_decoded_web():
    assert decoded_web("http://35.247.220.8/", "ubuntu") == 10
    assert decoded_web("http://35.247.220.8/", "apache") == 19
    assert decoded_web("http://35.247.220.8/", "linux") == 0