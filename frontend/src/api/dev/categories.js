export default {
  fetchCategories () {
    return Promise.resolve([{
      id: 1,
      name: 'Masken'
    },{
      id: 2,
      name: 'FFP2 / FFP3 Schutzmasken'
    },{
      id: 3,
      name: 'Kategorie 3'
    },{
      id: 4,
      name: 'Kategorie 4'
    },{
      id: 5,
      name: 'Kategorie 5'
    }])
  }
}