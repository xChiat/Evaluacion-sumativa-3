/*==============================================================*/
/* Table: CLIENTE */
/*==============================================================*/
create table CLIENTE
(
IDCLIENTE int not null auto_increment,
RUNCLIENTE varchar(10),
NOMBRECLIENTE varchar(15),
APELLIDOCLIENTE varchar(15),
TELEFONOCLIENTE varchar(10),
CORREOCLIENTE varchar(30),
primary key (IDCLIENTE)
);
/*==============================================================*/
/* Table: FICHA */
/*==============================================================*/
create table FICHA
(
IDFICHA int not null,
IDRECECPCION int not null,
IDMASCOTA int not null,
NUMEROFICHA int,
FECHAFICHA date,
primary key (IDFICHA)
);
/*==============================================================*/
/* Table: MASCOTAS */
/*==============================================================*/
create table MASCOTAS
(
IDMASCOTA int not null,
IDTIPO int,
IDCLIENTE int not null,
NOMBREMASCOTA varchar(25),
EDADMASCOTA int,
primary key (IDMASCOTA)
);
/*==============================================================*/
/* Table: RECEPCIONISTA */
/*==============================================================*/
create table RECEPCIONISTA
(
IDRECECPCION int not null auto_increment,
RUNRECEPCION varchar(10),
NOMBRERECEPCION varchar(15),
APELLIDORECEPCION varchar(15),
CLAVE varchar(32),
primary key (IDRECECPCION)
);
/*==============================================================*/
/* Table: TIPOMASCOTA */
/*==============================================================*/
create table TIPOMASCOTA
(
IDTIPO int not null,
DESCRIPCIONTIPO varchar(20),
primary key (IDTIPO)
);
alter table FICHA add constraint FK_GESTIONA foreign key (IDRECECPCION)
references RECEPCIONISTA (IDRECECPCION) on delete restrict on update restrict;
alter table FICHA add constraint FK_TIENE foreign key (IDMASCOTA)
references MASCOTAS (IDMASCOTA) on delete restrict on update restrict;
alter table MASCOTAS add constraint FK_ES_UN foreign key (IDTIPO)
references TIPOMASCOTA (IDTIPO) on delete restrict on update restrict;
alter table MASCOTAS add constraint FK_TIENEN foreign key (IDCLIENTE)
references CLIENTE (IDCLIENTE) on delete restrict on update restrict;