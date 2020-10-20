py -m pip install --upgrade pip
py -m pip install --user virtualenv
py -m venv env
.\env\Scripts\activate
py -m pip install --upgrade pip
for /F "tokens=*" %%A in (requirements.txt) do pip install %%A
pip install 
