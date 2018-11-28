import React, { Component } from 'react';

class item extends Component{
	constructor(props){
		super(props);
	}

	handleItemClick(){
		console.log('item tab has been clicked');
	}

	render(){
		return (
			<div>This is the item tab</div>
			);
	}
}
export default item;