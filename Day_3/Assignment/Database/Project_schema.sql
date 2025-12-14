
CREATE DATABASE IF NOT EXISTS sunbeam_online_portal;
USE sunbeam_online_portal;

CREATE TABLE IF NOT EXISTS User(
	email VARCHAR(100) NOT NULL UNIQUE,
	password VARCHAR(255),
	role ENUM('Student','Admin') DEFAULT 'student'
);

CREATE TABLE IF NOT EXISTS Course(
	course_id INT primary key auto_increment,
	course_name VARCHAR(100) not NULL,
	description VARCHAR(255) not NULL,
	fees int,
	start_date date,
	end_date date,
	video_expire_days int
);


CREATE TABLE IF NOT EXISTS  Student(
 reg_no INT primary key auto_increment,
 name VARCHAR(100) NOT NULL,
 email VARCHAR(100) NOT NULL,
 course_id int NOT NULL,
 Mobile_no VARCHAR(15),
 profile_pic blob,
 foreign key (email) references User(email),
 foreign key(course_id) references Course(course_id)
) ;

create table IF NOT EXISTS Videos(
video_id int primary key auto_increment,
course_id int,
title varchar(100) not null,
description varchar(255) not null,
youtube_url varchar(255) not null,
added_at Datetime default current_timestamp,
foreign key (course_id) references Course(course_id) on delete cascade
);

