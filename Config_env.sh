#en GEEKOM 
eval "$(oh-my-posh init bash --config c:/oh-my-posh/themes/0_raa.omp.json)" 
. C:/Users/RafaelAlbesaAlcón/Documents/2023-CodigoPython/PythonEnviroments/Env_Tokio1/Scripts/activate
#En el Zbook
eval "$(oh-my-posh init bash --config c:/oh-my-posh/themes/0_raa.omp.json)" 
. C:/Users/rafalbe/2023-CodigoPython/PythonEnviroments/Env_Tokio1/Scripts/activate



#Instalar paquetes
#1.- Actualizamos pip
python -m install pip --upgrade pip

#2.- Vemos lo que hay instalado en el venv (Sólo lo listará por pantalla)
python -m pip freeze
#3.- Instalamos a partir de un fichero de requerimientos.
python -m pip install -r requeriments.txt

#4.- Actualizamos el fichero de requeriments
python -m pip freeze > requeriments.txt

#5.- Para instalar un paquete
python -m pip install numpy