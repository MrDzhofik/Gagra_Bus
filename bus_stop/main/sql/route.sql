CREATE TABLE Town
(
    id         integer PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name       text NOT NULL,
);

CREATE TABLE Route
(
    id integer PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name text NOT NULL,
    number integer NOT NULL,
    town integer REFERENCES Town(id),
);
