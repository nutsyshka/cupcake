SELECT * FROM mydb.user;
SELECT * FROM mydb.company;
SELECT * FROM mydb.collectivecontract;
SELECT * FROM mydb.companyworker;
SELECT * FROM mydb.individual;
SELECT * FROM mydb.individualcontract;

INSERT INTO mydb.user VALUES (1, 'Dasha', 'Oreshkova', 'Dmitrievna', '123456', 'log', 'qwerty', 0);
INSERT INTO mydb.user VALUES (2, 'Rover', 'Book', 'Alpha', '12356', 'logi', 'qwerty123', 1);

INSERT INTO mydb.company VALUES (6, '678', 'Plex', 'GP', 'Game123', '5678', 'Mathematic', 1);

INSERT INTO mydb.collectivecontract VALUES (1, CURRENT_DATE, '11:11:11', 1000, 1, 100, 200, 300);

INSERT INTO mydb.companyworker VALUES (1, 'Dasha', 'Oreshkova', 'Dmitrievna', '19', 4, 1);

INSERT INTO mydb.individual VALUES (6, 'Dasha', 'Oreshkova', 'Dmitrievna', 19, 4, 'PersicSt', '823534123', 2);

INSERT INTO mydb.individualcontract VALUES (2, CURRENT_DATE, '16:11:11', 1000, 2751, 1);




