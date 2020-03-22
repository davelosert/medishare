export default {
  fetchCategories () {
    return Promise.resolve([{
      id: 1,
      name: 'OP-Masken',
      image: 'illustration-op-mask.svg'
    },{
      id: 2,
      name: 'FFP2 / FFP3 Schutzmasken',
      image: 'illustration-ffp-mask.svg'
    },{
      id: 3,
      name: 'Handschuhe',
      image: 'illustration-handschuh.svg'
    },{
      id: 4,
      name: 'Schutzbrillen',
      image: 'illustration-schutzbrille.svg'
    },{
      id: 5,
      name: 'Desinfektionsmittel',
      image: 'illustration-desinfektionsmittel.svg'
    },{
      id: 6,
      name: 'Schutzkleidung',
      image: 'illustration-schutzkleidung.svg'
    }
  ])
  }
}