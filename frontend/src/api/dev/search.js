export default {
  search ({categoryId, count, date}) {
    console.log(`Searching for ${count} of ${categoryId} until ${date}`)
    
    return Promise.resolve({
      success: true,
      data: {
        isAlternate: true,
        isCombination: true,
        results: [{
          giverId: 1,
          giverName: 'Tattoostudio Tintenrausch',
          itemCount: 30,
          distance: 3400, // distance in meters
          availability: 0 // 0 for now else date
        },{
          giverId: 2,
          giverName: 'Tattoostudio Tintenrausch',
          itemCount: 70,
          distance: 4100, // distance in meters
          availability: 0 // 0 for now else date
        },{
          giverId: 3,
          giverName: 'Privatperson',
          itemCount: 2,
          distance: 1200, // distance in meters
          availability: 0 // 0 for now else date
        },]
      }
    })
  }
}