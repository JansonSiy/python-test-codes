-- car table needs to be on top because person table will use it's id
create table car (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    make VARCHAR(100) NOT NULL,
    model VARCHAR(100) NOT NULL,
    price NUMERIC(19, 2) NOT NULL
);

create table person (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    gender VARCHAR(7) NOT NULL,
    email VARCHAR(100),
    date_of_birth DATE NOT NULL,
    country_of_birth VARCHAR(50) NOT NULL,
    car_id BIGINT REFERENCES car (id),
    -- references the id of the car table
    UNIQUE(car_id)
    -- a car can only be only owned by one person
);

insert into person (first_name, last_name, gender, email, date_of_birth, country_of_birth) values ('Jan', 'Siy', 'Male', 'jan@email.com', '1994-10-05', 'Philippines');
insert into person (first_name, last_name, gender, email, date_of_birth, country_of_birth) values ('Jeff', 'Smith', 'Male', 'jeff@email.com', '1993-09-16', 'USA');
insert into person (first_name, last_name, gender, email, date_of_birth, country_of_birth) values ('Nikka', 'Goot', 'Female', 'nikka@email.com', '1995-02-15', 'Japan');

insert into car (make, model, price) values ('Honda', 'City', '87665.38');
insert into car (make, model, price) values ('Toyota', 'Corolla', '17622.69');