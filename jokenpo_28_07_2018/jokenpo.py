MASTER_OPCOES_JOGADOR_1 = {
    'pedra': {
        'pedra': 'empate',
        'papel': 'jogador2',
        'tesoura': 'jogador1'
    },
    'papel': {
        'papel': 'empate',
        'tesoura': 'jogador2',
        'pedra': 'jogador1'
    },
    'tesoura': {
        'tesoura': 'empate',
        'pedra': 'jogador2',
        'papel': 'jogador1',
    },

}


def jokenpo(jogador1, jogador2):
    return MASTER_OPCOES_JOGADOR_1.get(jogador1, {}).get(jogador2, 'invalido')
