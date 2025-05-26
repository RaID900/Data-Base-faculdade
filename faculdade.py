create database db_sfaculdade;
use db_sfaculdade;
show tables;

create table tbl_professor (
	id int not null primary key auto_increment,
    nome varchar (100) not null,
    cpf varchar (18) not null,
    data_nascimento date not null,
    unique index (id)
);
create table tbl_curso (
	id int not null primary key auto_increment,
    nome_curso varchar(20) not null,
	codigo float not null,
    duracao varchar (30) not null,
    unique index (id)
);

create table tbl_aluno (
	id int not null primary key auto_increment,
    nome varchar(100) not null,
    cpf varchar (18) not null,
    data_nascimento date not null,
    matricula float not null,
    id_curso int not null,
    
    constraint fk_aluno_curso
    foreign key (id_curso)
    references tbl_curso (id),
    unique index (id)
);
create table tbl_endereco_aluno (
	id int not null primary key auto_increment,
    cep varchar (50) not null,
    cidade varchar (50) not null,
    estado varchar (50) not null,
    pais varchar (50) not null,
    id_aluno int not null,

	constraint fk_aluno_endereco_aluno
    foreign key (id_aluno)
    references tbl_aluno (id),
	unique index (id)
);
create table tbl_email_aluno (
	id int not null primary key auto_increment,
    email varchar (255) not null,
    id_aluno int not null,
    
    constraint fk_aluno_email_aluno
    foreign key (id_aluno)
	references tbl_aluno (id),
    unique index (id)
);
create table tbl_telefone_aluno (
	id int not null primary key auto_increment,
    telefone varchar(15) not null,
    id_aluno int not null,
    
    constraint fk_aluno_telefone_aluno
    foreign key (id_aluno)
    references tbl_aluno (id),
	unique index (id)
);
create table tbl_endereco_professor (
	id int not null primary key auto_increment,
    cep varchar (50) not null,
    cidade varchar (50) not null,
    estado varchar (50) not null,
    pais varchar (50) not null,
    id_professor int not null,

	constraint fk_professor_endereco_professor
    foreign key (id_professor)
    references tbl_professor (id),
	unique index (id)
);
create table tbl_email_professor (
	id int not null primary key auto_increment,
    email varchar (255) not null,
    id_professor int not null,
    
    constraint fk_professor_email_professor
    foreign key (id_professor)
	references tbl_professor (id),
    unique index (id)
);
create table tbl_telefone_professor (
	id int not null primary key auto_increment,
    telefone varchar(15) not null,
    id_professor int not null,
    
    constraint fk_professor_telefone_professor
    foreign key (id_professor)
    references tbl_professor (id),
	unique index (id)
);
create table tbl_materia (
	id int not null primary key auto_increment,
    nome_materia varchar (30) not null,
    codigo float not null,
    carga_horaria float not null,
	id_professor int not null,
    
    constraint fk_professor_materia
    foreign key (id_professor)
    references tbl_professor (id),
    unique index (id)
);
create table tbl_nota (
	id int not null primary key auto_increment,
    data_avaliacao date not null,
    id_aluno int not null,
	id_materia int not null,
    nota float not null,
    
    constraint fk_aluno_nota
    foreign key (id_aluno)
    references tbl_aluno (id),
    
    constraint fk_materia_nota
    foreign key (id_materia)
    references tbl_materia (id),
	unique index (id)
);
create table tbl_turma (
	id int not null primary key auto_increment,
    codigo_turma float not null,
    id_aluno int not null,
    id_professor int not null,
    id_materia int not null,
    
    constraint fk_aluno_turma
    foreign key (id_aluno)
	references tbl_aluno (id),
    
    constraint fk_professor_turma
    foreign key (id_professor)
    references tbl_professor (id),
    
    constraint fk_materia_turma
    foreign key (id_materia)
    references tbl_materia (id),
    unique index (id)
);
insert into tbl_curso (id, nome_curso, codigo, duracao)
values (1, 'Medicina', '5937', '5,5');

insert into tbl_curso (id, nome_curso, codigo, duracao)
values (2, 'Administração', '1234', '2,5');
