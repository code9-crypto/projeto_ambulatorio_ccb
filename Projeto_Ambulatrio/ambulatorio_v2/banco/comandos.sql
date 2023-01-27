use ambulatorio;

select * from tb_pacientes;
select identidade_atendido from tb_pacientes where identidade_atendido like 'M%' order by identidade_atendido desc limit 1;
select nome from tb_pacientes where nome like 'eli rosa%';
alter table tb_pacientes add identidade_atendido char(3) not null;
alter table tb_pacientes auto_increment = 1;
update tb_pacientes set identidade_atendido = 'C-1' where idpacientes = 3;
delete from tb_pacientes;

select * from tb_profissionais;
select concat(upper(nome_completo),":", rp) as identificacao from tb_profissionais;
alter table tb_profissionais modify rp varchar(25) not null;
delete from tb_profissionais;
alter table tb_profissionais auto_increment=1;
insert into tb_profissionais (nome_completo, profissao, crm) values ("Adriano saldanha","médico","567891");

select * from tb_fichas_de_atendimentos;
select idatendimentos, nome_atendido from tb_fichas_de_atendimentos where reavaliacao = 'SIM';
delete from tb_fichas_de_atendimentos;
alter table tb_fichas_de_atendimentos modify glicemia varchar(5);
alter table tb_fichas_de_atendimentos auto_increment = 1;
update tb_fichas_de_atendimentos set identificacao_profissional = 'ADRIANO SALDANHA CRM:567891, RAFAEL BARBOSA CRM:345678' where idatendimentos = 3;

select * from tb_contas_profissional;
insert into tb_contas_profissional (usuario, senha) values  ("ambulatorio", "ambulatorio");
delete from tb_contas_profissional;
alter table tb_contas_profissional auto_increment = 1;

select nome_evento from tb_eventos order by nome_evento;
insert into tb_eventos (nome_evento) values ("Reunião de Aconselhamento Ministerial");


select distinct nome_atendido from tb_fichas_de_atendimentos;

select idpacientes, nome, ministerio, cidade, estado, pais, count(nome_atendido) as quantidade from tb_pacientes inner join 
tb_fichas_de_atendimentos on tb_fichas_de_atendimentos.tb_pacientes_fkpacientes_atendimento = tb_pacientes.fkpacientes_atendimento
where tb_fichas_de_atendimentos.nome_atendido = 'Elizeu Rosa França';

select count(distinctrow tb_pacientes_fkpacientes_atendimento), nome, ministerio, cidade, estado, pais  from tb_fichas_de_atendimentos inner join tb_pacientes on 
tb_fichas_de_atendimentos.tb_pacientes_fkpacientes_atendimento = tb_pacientes.fkpacientes_atendimento;

select count(distinct nome) from tb_pacientes inner join tb_fichas_de_atendimentos 
on tb_pacientes.nome = tb_fichas_de_atendimentos.nome_atendido;

select nome_atendido, count(*) from tb_fichas_de_atendimentos where nome_atendido = 'Eli Rosa França';

select distinct nome from tb_pacientestb_paciente;

create table tb_eventos(


idevento int not null auto_increment,
nome_evento varchar(45) not null,
primary key(idevento)
);

select * from tb_eventos order by nome_evento;
delete from tb_eventos;
alter table tb_eventos auto_increment = 1;