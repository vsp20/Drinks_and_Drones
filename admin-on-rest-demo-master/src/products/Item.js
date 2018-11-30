import React, { Component } from 'react';

class Item extends Component{
	constructor(props){
		super(props);
	}


	render(){
		const {
			id,
			name,
			imageSrc // This is the image picture
		} = this.props;
		return (
		<div className="drink" id={id}>
            <div className="drinkHeader">
                <h4 className="drinkTitle">{name}</h4>
            </div>
            <div className="drinkBody">
                <div className="drinkIcon">
                    <img src={imageSrc} width="200" height="200"/>
                </div>
            </div>
        </div>
			);
	}
}
export default Item;