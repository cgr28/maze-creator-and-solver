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