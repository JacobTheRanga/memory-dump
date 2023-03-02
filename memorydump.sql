drop user if exists 'memorydump'@'localhost';
create user 'memorydump'@'localhost' identified by 'memorydump';

drop database if exists memorydump;
create database memorydump;
use memorydump;

drop table if exists items;
create table items(
    id int not null auto_increment,
    item varchar(255) not null,
    primary key (id)
);

drop table if exists tags;
create table tags(
    id int not null auto_increment,
    tag varchar(255) not null,
    primary key (id)
);

drop table if exists itemtags;
create table itemtags(
    itemid int not null,
    tagid int not null,
    primary key (itemid, tagid),
    foreign key (itemid) references items (id),
    foreign key (tagid) references tags (id)
);

grant all on memorydump.* to memorydump@localhost;