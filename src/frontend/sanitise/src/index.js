import React from 'react';
import { render } from 'react-dom';
import * as apis from './APILoader.js';

var testData = apis.objectLoader("http://localhost:5000/test");
console.log(testData);

let bookList = [
	{"title": "Hunger", "author": "Roxane Gay", "pages": 320},
	{"title": "The Sun Also Rises", "author": "Ernest Hemingway", "pages": 260},
	{"title": "White Teeth", "author": "Zadie Smith", "pages": 480},
	{"title": "Cat's Cradle", "author": "Kurt Vonnegut", "pages": 304}
]

const Book = ({title, author, pages, freeBookmark}) => {
	return (
		<section>
			<h2>{title}</h2>
			<p>by: {author}</p>
			<p>Pages: {pages} pages</p>
			<p>Free Bookmark Today: {freeBookmark ? 'yes!': 'no!'}</p>
		</section>
	)
}

class Library extends React.Component {
	
	state = { 
		open: true,
		freeBookmark: false
	}

	toggleOpenClosed = () => {
		this.setState(prevState => ({
			open: !prevState.open
		}))
	}
	render() {
		const books = this.props.books;
		return (
			<div>
				<h1>The library is {this.state.open ? 'open' : 'closed'}</h1>
				<button onClick={this.toggleOpenClosed}>Change</button>
				{books.map(
					(book, i) => 
						<Book 
							key={i}
							title={book.title} 
							author={book.author} 
							pages={book.pages}
							freeBookmark={this.state.freeBookmark}/>
				)}
			</div>
		)
	}
}



render(
	<Library books={bookList}/>, 
	document.getElementById('root')
)
