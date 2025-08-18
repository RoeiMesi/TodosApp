export const sortTodos = (todos, preference) => {
    switch(preference) {
        case "High to Low":
            return [...todos].sort((a,b) => b.priority.localeCompare(a.priority));

        case "Low to High":
            return [...todos].sort((a,b) => a.priority.localeCompare(b.priority));

        default:
            return todos
    }
}