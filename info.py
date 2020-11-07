import streamlit as st

def header():
    st.markdown((
        'De notatie-wijzigingen zoals zijn geintroduceerd door Steven kunnen als volgt samengevat worden:  \n'
        '- De `↑` is een operator voor _macht_ functies en spreek je uit als _macht omhoog_.  \nDus `2↑3` is `8` en wordt gewoonlijk geschreven als `2³`.  \n'
        '- De `↓` is een operator voor _n-wortel_ functies en spreek je uit als _macht omlaag_.  \nDus `8↓3` is `2` en wordt gewoonlijk geschreven als `∛8`.  \n'
        '- De `⇓` is een operator voor _basis-n log_ functies en spreek je uit als _dubbel macht omlaag_.  \nDus `8⇓2` is `3` n wordt gewoonlijk geschreven als `²log8`.  \n'
        '- Het is mogelijk om `÷÷2` te schrijven, en komt overeen met `1÷1÷2=2`.  \nNet zoals `--2` overeenkomt met `0-0-2=2`.'        
        ),
        unsafe_allow_html=True
    )


def relations_power_root_log():
    st.markdown(f'Het leuke van de nieuwe notatie is dat het veel visueel duidelijker de relaties tussen macht, wortel en log weergeeft. Dus laten we de relaties samenvatten, om de betrokken patronen duidelijker te laten zien:')
    r0c0, r0c1, r0c2 = st.beta_columns(3)
    r0c0.success('Operator')
    r0c1.success('Om a te bepalen')
    r0c2.success('Om b te bepalen')

    r1c0, r1c1, r1c2 = st.beta_columns(3)
    r1c0.info('a+b  \n a-b')
    r1c1.info('(a+b)−b  \n (a−b)+b')
    r1c2.info('(a+b)−a  \n a−(a−b)')

    r2c0, r2c1, r2c2 = st.beta_columns(3)
    r2c0.info('a×b  \n a÷b')
    r2c1.info('(a×b)÷b  \n (a÷b)×b')
    r2c2.info('(a×b)÷a  \n a÷(a÷b)')

    r3c0, r3c1, r3c2 = st.beta_columns(3)
    r3c0.info('a↑b  \n a↓b  \n a⇓b')
    r3c1.info('(a↑b)↓b  \n (a↓b)↑b  \n b↑(a⇓b)')
    r3c2.info('(a↑b)⇓a  \n a⇓(a↓b)  \n a↓(a⇓b)')
 
def usage_example():
    st.markdown((
       'Je stopt een hoeveelheid geld `g` op een bankrekening met een rente van `3%`, na `10` jaar heb je dan  \n'
       '> `g×1.03↑10` (= `€134` als je start met `€100`)  \n\n'
       'Noem de rente (`1.03` in dit geval) `r`, en het aantal jaar `j`:  \n'
       '> `g×r↑j`  \n\n'
       '__Hoeveel moet je sparen om `1000` te hebben na `10` jaar?__  \n'
       '> `g×1.03↑10 = 1000`  \n\n'
       'Deel beide kanten met `1.03↑10`  \n'
       '> `g = 1000 ÷ 1.03↑10`  \n\n'
       'wat overeenkomt met `€744`  \n\n'
       '__Met welke rente verdubbeld mijn geld in `10` jaar?__  \n'
       '> `g×r↑10 = 2×g`  \n\n'
       'Deel beide kanten door `g`  \n'
       '> `r↑10 = 2`  \n\n'
       'neem de `10e` wortel aan beide kanten:  \n'
       '> `(g↑10)↓10 = 2↓10`  \n'
       '`r = 2↓10`  \n\n'
       'wat overeen komt met `1.072`, oftewel een rente van `7.2%`  \n\n'
       '__Hoeveel jaar moet ik sparen om mijn geld te vermenigvuldigen met een rente van `3%`?__  \n'
       '> `g×1.03↑j = 2×g`  \n\n'
       'Verdeel beide kanten door `g`  \n'
       '> `1.03↑y = 2`  \n\n'
       'en neem de log aan beide kanten  \n'
       '> `(1.03↑j)⇓1.03 = 2⇓1.03`  \n'
       '`j = 2⇓1.03`  \n\n'
       'wat overeen komt met `23.45` (jaren)'
    ))