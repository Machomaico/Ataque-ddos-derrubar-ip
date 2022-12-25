echo "Iniciando  instalação..."
sleep 2 
pkg install python -y 
clear
pip install colorama 
clear
pip install tqdm 
clear
echo "instalação completa.."
var1="1"
echo "Iniciar script"
echo "1) Sim"
echo "2) Sair"
read -p ">> " resp
if [ "$resp" == "$var1" ]
then
python3 biyivi_ddos.py
else
echo "Para iniciar a script: python iniciar_ataque_ddos.py"
echo ":D"
fi
