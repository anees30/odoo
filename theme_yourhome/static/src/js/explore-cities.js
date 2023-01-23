/** @odoo-module **/

import publicWidget from 'web.public.widget';

publicWidget.registry.YhCities = publicWidget.Widget.extend({
    selector: '.explore-cities',
    start() {
        console.log('Yh Cities Start')
        console.log(this.el)
        console.log(this.el.querySelector('#yh-cities-row'))
        let citiesRow = this.el.querySelector('#yh-cities-row')
        if(citiesRow) {
            citiesRow.innerHTML = '<div>-----this is from js-------</div>'
            this._rpc({
                route: '/cities/',
                params: {}
            }).then(data => {
                let html = ``
                data.forEach(city => {
                    html += `<div class="col-lg-3 mb-3">
                    <div class="d-flex align-items-center">
                        <div class="me-3 rounded">
                            <img class="country-image rounded" src="data:image/png;base64,${city.image}" alt="City Name"/>
                        </div>
                        <div>
                            <h5 class="mb-0">${city.state_id ? city.state_id[1] : ''}</h5>
                            <div>${city.country_id ? city.country_id[1] : ''}</div>
                        </div>
                    </div>
                </div>` 
                })
                citiesRow.innerHTML = html
            })
        }
        
    },
});

export default publicWidget.registry.YhCities;
