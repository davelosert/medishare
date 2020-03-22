export default {
  fetchCategories() {
    return fetch('/api/categories/')
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        return data;
      });
  }
}