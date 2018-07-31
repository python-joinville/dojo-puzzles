import pytest

from jokenpo import jokenpo


@pytest.mark.parametrize('jogada1,jogada2,esperado', [
    ('pedra', 'pedra', 'empate'),
    ('pedra', 'tesoura', 'jogador1'),
    ('pedra', 'papel', 'jogador2'),
    ('papel', 'papel', 'empate'),
    ('papel', 'tesoura', 'jogador2'),
    ('papel', 'pedra', 'jogador1'),
    ('tesoura', 'tesoura', 'empate'),
    ('tesoura', 'papel', 'jogador1'),
    ('tesoura', 'pedra', 'jogador2'),
    ('pedra', 'carro', 'invalido'),
    ('carro', 'preda', 'invalido'),
    ('carro', 'pedra', 'invalido')
])
def test_jogadas(jogada1, jogada2, esperado):
    resultado = jokenpo(jogada1, jogada2)
    assert resultado == esperado
