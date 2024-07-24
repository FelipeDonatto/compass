def getColumns(): 
    with open('./actors.csv') as f:
        columns = f.readline().split(",")
        return ",".join(columns)


def etapa01():
    f1 = open("./etapa-1.txt", "a")
    f1.write(getColumns())
    
    with open('./actors.csv') as f:
        next(f)
        mostMovies = [0,0,0,0,0]
        for line in f:
            if "Robert Downey" in line.split(",")[0]:
                line = line.replace("Robert Downey, Jr.", "Robert Downey Jr.")
            treatedLine = line.strip("\n").split(",")
            if int(treatedLine[2]) > int(mostMovies[2]):
                mostMovies = treatedLine
        f1.write(",".join(mostMovies))
        return(mostMovies)

def etapa02():
    f2 = open("./etapa-2.txt", "a")
    f2.write("Média de receita bruta por ator")
    
    with open('./actors.csv') as f:
        next(f)
        count = 1;
        totalGross = 0;
        for line in f:
            if "Robert Downey" in line.split(",")[0]:
                line = line.replace("Robert Downey, Jr.", "Robert Downey Jr.")
            treatedLine = line.strip("\n").split(",")
            totalGross = totalGross + float(treatedLine[5])
            count += 1
        print(round(totalGross / count,2))
        f2.write("\n")
        f2.write(str(round(totalGross / count,2)))
        return(round(totalGross / count,2))

def etapa03():
    f3 = open("./etapa-3.txt", "a")
    f3.write("Ator/Atriz, Receita bruta")
    with open('./actors.csv') as f:
        next(f)
        higherAverageRevenue = [0,0,0,0,0]
        actor = []
        for line in f:
            if "Robert Downey" in line.split(",")[0]:
                line = line.replace("Robert Downey, Jr.", "Robert Downey Jr.")
            treatedLine = line.strip("\n").split(",")
            if float(treatedLine[3]) > float(higherAverageRevenue[3]):
                higherAverageRevenue = treatedLine
        f3.write("\n")
        f3.write(f"{higherAverageRevenue[0]}, {higherAverageRevenue[3]}")
        print(higherAverageRevenue)
        return(higherAverageRevenue)
        
def etapa04():
    with open('./actors.csv') as f:
        f4 = open("./etapa-4.txt", "a")
        next(f)
        movies = set()
        movieList = []
        for line in f:
            if "Robert Downey" in line.split(",")[0]:
                line = line.replace("Robert Downey, Jr.", "Robert Downey Jr.")
            treatedLine = line.strip("\n").split(",")
            movies.add(treatedLine[4])
            
        for item in movies:
            movieList.append(dict({"movie": item, "count": (open('./actors.csv').read().count(item))}))
        for index, movie in enumerate(sorted(movieList, key=lambda x: (x["count"], x["movie"]), reverse=True)):
            f4.write(f"{index} - O filme {movie['movie']} aparece {movie['count']} vez(es) no dataset\n")
        return (sorted(movieList, key=lambda x: (x["count"], x["movie"]), reverse=True))
        

def etapa05():
    with open('./actors.csv') as f:
        f5 = open("./etapa-5.txt", "a")
        f5.write("Nome - Receita bruta")
        
        next(f)
        actorList = []
        for line in f:
            if "Robert Downey" in line.split(",")[0]:
                line = line.replace("Robert Downey, Jr.", "Robert Downey Jr.")
            treatedLine = line.strip("\n").split(",")
            actorList.append(dict({"actor": treatedLine[0], "totalGross": treatedLine[1]}))
            
        for actor in sorted(actorList, key=lambda x: (x["totalGross"]), reverse=True):
            f5.write("\n")
            f5.write(f"{actor['actor']} - {actor['totalGross']}")
        return sorted(actorList, key=lambda x: (x["totalGross"]), reverse=True)

etapa05()


