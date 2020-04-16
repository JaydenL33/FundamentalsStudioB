import React from 'react';
import ReactDOM from 'react-dom';
import * as apis from './APILoader.js';

apis.ghibliapi();

let skiData = {
	total: 2,
	powder: 20,
	backCountry: 10,
	goal: 100
}

class SkiDayCounter extends React.Component {
	render() {
		return (
			<section>
				<div>

				</div>
			</section>
		)
	}
}

ReactDOM.render(
	<SkiDayCounter
		total={skiData.total}
		powder={skiData.powder}
		backCountry={skiData.backCountry}
			/>, 
	document.getElementById('root')
)


