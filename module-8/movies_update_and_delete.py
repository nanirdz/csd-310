def show_films(cursor, title) :
    # method to execute an inner join on all tables,
    #   iterate over the dataset and output the results to the terminal window.

    # inner join query
    cursor.execute("select film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' from film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")

    # get the results from the cursor object
    films = cursor.fetchall()

    print("\n -- {} --".format(title))

    # iterate over the film data set and display the results
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

# insert film record
    INSERT INTO film(film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) 
    VALUES('M3GAN', '2022', '132', 'Gerard Johnstone', (SELECT studio_id FROM studio WHERE studio_name = 'Universal Pictures'),(SELECT genre_id FROM genre WHERE genre_name = 'Horror') );

# update Alien film genre
     UPDATE film, genre
     SET genre_name = 'Horror'
     WHERE film_name = 'Aliens';

# delete Gladiator movie
    DELETE FROM film
    WHERE film_name = 'Gladiator';