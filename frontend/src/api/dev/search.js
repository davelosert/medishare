export default {
  search({ category, count, date }) {
    console.log(`Searching for ${count} of ${category.name} until ${date}`)

    return Promise.resolve({
      success: true,
      data: [{
        isCombination: true,
        items: [{
          giverId: 1,
          giverName: 'Tattoostudio Tintenrausch',
          itemCount: 30,
          distance: 3400, // distance in meters
          availability: 0 // 0 for now else date
        }, {
          giverId: 2,
          giverName: 'Tattoostudio Tintenrausch',
          itemCount: 70,
          distance: 4100, // distance in meters
          availability: 0 // 0 for now else date
        },]
      },
      {
        isCombination: false,
        items: [{
          giverId: 3,
          giverName: 'Privatperson',
          itemCount: 2,
          distance: 1200, // distance in meters
          availability: 0 // 0 for now else date
        }]
      }
      ]
    })
  }
}