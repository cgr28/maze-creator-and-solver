export const getSolversQuery = (checked, solverTypes) => {
    let solvers = []
    for (let i = 0; i < checked.length; i++) {
        if (checked[i]) {
            solvers.push(solverTypes[i].value)
        }
    }
    if (solvers.length === 0) {
        return ""
    } else if (solvers.length === 1) {
        return `?solver=${solvers[0]}`
    } else {
        let query = `?solver=${solvers[0]}`
        for (let i = 1; i < solvers.length; i++) {
            query += `&solver=${solvers[i]}`
        }
        return query
    }
}

export const solverTypes = [{name: "Breadth First Search", value: "breadth-first-search"}, {name: "Depth First Search", value: "depth-first-search"}, {name: "Best First Search", value: "best-first-search"}, {name: "A-Star", value: "a-star"}, {name: "None", value: "none"}]