create database Classes;   
use Classes;

create table detetive(
	id integer auto_increment primary key,
	nome varchar(200),
	sobrenome varchar(100),
	cargo varchar(200),
	participacaoAnterior varchar(100)
);

create table alianca (
    id int primary key auto_increment,
    detetive_id varchar(200)
);

create table if not exists peca(
    id integer auto_increment,
    detetiveResponsavel varchar(100), 
    descricaoPeca varchar(500),
    primary key(id)
    );
    
create table if not exists competicao(
    id integer auto_increment,
    listaParticipantes varchar(600),
    dataCompeticao varchar(100),
    primary key(id)
);

create table if not exists estrategia(
    id integer auto_increment,
    detetive_id varchar(200), 
    listaAcoes varchar(300),
    primary key(id)
);

create table if not exists regras(
    id integer auto_increment,
    restricoesLocal varchar(300),
    duracao varchar(200),
    primary key(id)
);

create table if not exists ranking(
    id integer auto_increment,
    listaDetetives varchar(400),
    pontuacoes varchar(400),
    primary key(id)
);

create table if not exists trofeu(
    id integer auto_increment,
    detetive_id varchar(200),
    anoVitoria varchar(100),
    fraseVitoria varchar(200),
    primary key(id)
);
