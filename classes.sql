create database Classes;
use Classes;


create table Detetive(
	id integer auto_increment primary key,
    nome varchar(100),
    sobrenome varchar(100),
    cargo varchar(100),
    participacaoAnterior varchar(100)
);

create table Alianca(
	id integer auto_increment primary key,
	detetivesAliados varchar(150),
    foreign key (detetivesAliados) references Detetive(id) 
);

create table Peca(
	id integer auto_increment primary key,
	detetiveResponsavel varchar(100),
    descricaoPeca varchar(200),
	foreign key (detetiveResponsavel) references Detetive(id) 
);

create table Estrategia(
	id integer auto_increment primary key,
	detetive varchar(100),
    listaAcoes varchar(200),
	foreign key (detetive) references Detetive(id) 
);

create table Competicao(
	id integer auto_increment primary key,
	listaParticipantes varchar(150),
    dataCompeticao date,
	foreign key (listaParticipantes) references Detetive(id) 
);

create table Regras(
	id integer auto_increment primary key,
	restricoesLocal varchar(200),
    duracao varchar(200)
);

create table Ranking(
	id integer auto_increment primary key,
	listaDetetives varchar(200),
    pontuacoes varchar(200),
	foreign key (listaDetetives) references Detetive(id) 
);

create table Trofeu(
	id integer auto_increment primary key,
	detetiveVencedor varchar(100),
	anoVitoria date,
    fraseVitoria varchar(200),
	foreign key (detetiveVencedor) references Detetive(id) 
);

select * from Detetive;
select * from Alianca;
select * from Peca;
select * from Estrategia;
select * from Competicao;
select * from Regras;
select * from Ranking;
select * from Trofeu;
