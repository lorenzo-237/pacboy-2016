diapo = open('cssdiapo.txt','w')
diapo.write("""
#balise
{

\tbackground: url("#chemin") no-repeat;

\twebkit-animation-name: #name;
\twebkit-animation-duration: #s;
\twebkit-animation-timing-function: linear;
\twebkit-animation-iteration-count: infinite;
\twebkit-animation-direction: normal;

\tmoz-animation-name: #name;
\tmoz-animation-duration: #s;
\tmoz-animation-timing-function: linear;
\tmoz-animation-iteration-count: infinite;
\tmoz-animation-direction: normal;

\tanimation-name: #name;
\tanimation-duration: #s;
\tanimation-timing-function: linear;
\tanimation-iteration-count: infinite;
\tanimation-direction: normal;

}

@-webkit-keyframes #name
{
\t#%{background-image: url("#chemin");}
\t#%{background-image: url("#chemin");}
}
@-moz-keyframes #name
{
\t#%{background-image: url("#chemin");}
\t#%{background-image: url("#chemin");}
}
@keyframes #name
{
\t#%{background-image: url("#chemin");}
\t#%{background-image: url("#chemin");}
}
""")
diapo.close()



