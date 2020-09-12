# Given a list of full paths to files, and a list of filenames to query,
# Report all the full paths that match that filename.



def finder(files, queries):
    cache = {}
    result = []
    
    for file in range(len(files)):
        cache[files[file]] = file
        
        for char in queries: 
            if file.endswith(char):
                result.append(file)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
