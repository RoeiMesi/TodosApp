import React, { useState, useEffect } from "react";

export default function TodoForm({ dispatch, editingTodo }) {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [priority, setPriority] = useState(1);

  useEffect(() => {
    if (editingTodo) {
      setTitle(editingTodo.title);
      setDescription(editingTodo.description);
      setPriority(editingTodo.priority);
    } else {
      clearForm();
    }
  }, [editingTodo]);

  const priorityLabels = {
    1: "Low",
    2: "Medium",
    3: "High",
  };

  const clearForm = () => {
    setTitle("");
    setDescription("");
    setPriority(1);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    clearForm();

    const todoData = {
      title,
      description,
      priority,
      completed: editingTodo ? editingTodo.completed : false
    };

    dispatch({
      type: editingTodo ? "UPDATE_TODO" : "ADD_TODO",
      payload: todoData,
    });
  };

  const handleCancel = () => {
    dispatch({ type: "CLEAR_EDITING_TODO" });
    clearForm();
  };

  return (
    <form onSubmit={handleSubmit} className="todo-form">
      <div>
        <label>Title</label>
        <input
          type="text"
          value={title}
          className="form-input"
          onChange={(e) => setTitle(e.target.value)}
        ></input>
        <label>Description</label>
        <textarea
          type="text"
          value={description}
          className="form-input"
          onChange={(e) => setDescription(e.target.value)}
        ></textarea>
        <fieldset className="priority-fieldset">
          <legend>Priority</legend>

          {Object.entries(priorityLabels).map(([value, label]) => (
            <label key={value} className="priority-label">
              <input
                type="radio"
                value={value}
                checked={priority === value}
                className="priority-input"
                onChange={(e) => setPriority(e.target.value)}
              ></input>
              {label}
            </label>
          ))}
        </fieldset>
      </div>
      <button type="submit" className="button">
        Submit
      </button>

      {editingTodo && (
        <button className="button" onClick={handleCancel}>
          Cancel Edit
        </button>
      )}
    </form>
  );
}
