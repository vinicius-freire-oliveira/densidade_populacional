import scrapy

class DensidadePopulacionalSpider(scrapy.Spider):
    name = 'densidade_populacional'
    start_urls = ['https://pt.wikipedia.org/wiki/Lista_de_pa%C3%ADses_por_densidade_populacional']

    def parse(self, response):
        # Encontra todas as tabelas na página
        tabelas = response.xpath('//table[contains(@class, "wikitable")]')
        self.log(f'Número de tabelas encontradas: {len(tabelas)}')

        # Itera sobre todas as tabelas encontradas
        for tabela in tabelas:
            # Itera sobre as linhas da tabela, começando da segunda linha (pula o cabeçalho)
            for linha in tabela.xpath('.//tr')[1:]:  # [1:] para pular o cabeçalho
                colunas = linha.xpath('.//td')
                self.log(f'Número de colunas na linha: {len(colunas)}')

                if len(colunas) >= 5:  # Verifica se há pelo menos 5 colunas
                    posicao = colunas[0].xpath('string()').get(default='').strip()
                    pais = colunas[1].xpath('string()').get(default='').strip()
                    populacao = colunas[2].xpath('string()').get(default='').strip()
                    area = colunas[3].xpath('string()').get(default='').strip()
                    densidade = colunas[4].xpath('string()').get(default='').strip()

                    # Adiciona logs para verificar os dados extraídos
                    self.log(f'Posição: {posicao}, País: {pais}, População: {populacao}, Área: {area}, Densidade: {densidade}')

                    # Cria um dicionário para armazenar os dados raspados
                    yield {
                        'Posição': posicao,
                        'País': pais,
                        'População': populacao,
                        'Área (km²)': area,
                        'Densidade (habitantes por km²)': densidade
                    }
