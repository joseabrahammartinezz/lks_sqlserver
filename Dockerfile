FROM python:3.10
ENV PYTHONUNBUFFERED 1
#### PREPARAMOS REQUISITOS PARA CONECTAR SQLSERVER

## INSTALAMOS ODBC DRIVER 17 QUE SE USA EN UBUNTU 18.04
RUN apt-get install curl
#apt-get install apt-transport-https
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list

RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17
# optional: for bcp and sqlcmd
sudo ACCEPT_EULA=Y apt-get install -y mssql-tools
echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
source ~/.bashrc
# optional: for unixODBC development headers
sudo apt-get install -y unixodbc-dev

#####  PARA EL BACKEND

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip
#RUN apt-get update && apt-get install -y libgdal-dev g++ --no-install-recommends && \
#    apt-get clean -y

RUN python -m pip install -r requirements.txt
COPY . /code/
