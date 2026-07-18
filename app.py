import streamlit as st
import spacy



nlp = spacy.load("pt_core_news_sm")


st.set_page_config(
    page_title="Classificador Banco Digital"
)


st.title("🏦 Classificador de Solicitações Bancárias")


st.write(
    "Digite uma solicitação do cliente e o sistema identificará o setor responsável."
)


texto = st.text_area(
    "Digite a mensagem do cliente:"
)


if st.button("Classificar"):


    if texto.strip() == "":

        st.warning(
            "Digite uma mensagem para analisar."
        )


    else:

        doc = nlp(texto.lower())

        bloqueio_cartao = [
            "bloquear",
            "bloqueio",
            "cartão",
            "perdi",
            "roubado"
        ]


        segunda_via_boleto = [
            "segunda via",
            "boleto",
            "fatura",
            "vencido"
        ]


        acesso = [
            "senha",
            "login",
            "acesso",
            "entrar"
        ]


        pagamento = [
            "pagamento",
            "pix",
            "transferência",
            "cobrança"
        ]

        dados_cadastrais = [
            "atualizar",
            "dados",
            "cadastro",
            "cadastrais",
            "alterar",
            "endereço"
        ]



        palavras = [
            token.text 
            for token in doc
        ]


        categoria = "Não identificado"


       
        for palavra in palavras:


            if palavra in bloqueio_cartao:

                categoria = "💳 Bloqueio de cartão"
                break


            elif palavra in segunda_via_boleto:

                categoria = "📄 Segunda via de boleto"
                break


            elif palavra in acesso:

                categoria = "🔑 Problema de acesso"
                break


            elif palavra in pagamento:

                categoria = "💰 Pagamentos"
                break

            elif palavra in dados_cadastrais:

                categoria = "📝 Atualização de dados cadastrais"
                break


        st.subheader("Resultado")

        st.success(
            categoria
        )


        st.write(
            "Texto analisado:"
        )

        st.write(texto)
