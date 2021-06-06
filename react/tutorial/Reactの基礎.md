# Reactの基礎
## 4.1 JSX
### 4.1.1 JavaScript式を埋め込む
#### コード
* 関数や変数を埋め込む
```jsx
function add(a, b) {
	return a + b;
}
function App() {
	const messate = 'React'
	return (
		<div>
			<p>Hello {message}</p>
		</div>
		<p>1 + 2 = { add(1, 2) }</p>
	);
}
```
* 属性値に式を埋めこむ
```jsx
function App() {
	const url = 'https://reactjs.org/';
	return <a href={url}>React</p>;
}
```
* 属性をまとめて埋め込む
  - スプレッド構文`...`を利用する
```jsx
function App() {
	const attrs = {
		src: './logo.jpg',
		alt: 'React'
	};
	return <img {...attrs} />;
	// <img src="./logo.jpg" alt="React">
}
```
### 4.1.2 JSXのルール
1. ルート要素は１つだけ定義できる
* 以下はNG
```jsx
function App() {
	return (
		<p>Hello React</p>
		<p>Hello Vue.js</p>
	);
}
```
* 正しくは`<div>`でラップする
```jsx
function App() {
	return (
		<div>
			<p>Hello React</p>
			<p>Hello Vue.js</p>
		</div>
	);
}
```
* 上記だとHTML構造が代わってしまうので、「フラグメント」という機能がある
```jsx
function App() {
	return (
		<>
			<p>Hello React</p>
			<p>Hello Vue.js</p>
		</>
	);
}
```
* すべてのタグを閉じる必要がある
  - ルート要素外に`<br>`などがあるとエラーになる
* class などの属性は利用できず、代替の属性を利用する必要がある
  - `class`はjsxで予約語となっているため、HTML属性としては`className`のうな代替を使う必要がある

```jsx
function App() {
	return <h1 className="heading">Hello React</h1>
}
```

## 4.2 コンポーネント
### 4.2.1 関数コンポーネントの定義
