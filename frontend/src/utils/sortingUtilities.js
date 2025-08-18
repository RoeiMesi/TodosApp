export const sortTodos = (todos, preference) => {
  const copy = [...todos];
  switch (preference) {
    case "High to Low":
      return copy.sort((a, b) => Number(b.priority) - Number(a.priority));
    case "Low to High":
      return copy.sort((a, b) => Number(a.priority) - Number(b.priority));
    default:
      return copy;
  }
};
