// Reactを利用する場合、必ずreactをimportする必要がある
import React from 'react';

// Appコンポーネント
function App() {
	// JSXというjavascriptの拡張(javascriptに独自の構文を拡張したもの)を利用すれば
	// javascriptにHTMLのような構文をかける。JSXはブラウザでは動作しないので通常のjavascriptに変換する
	// 必要があるが、Create React Appで作成した開発環境では変換も自動で行ってくれる。
	// そのため、こちら側では何もせずにJSXを利用できる
	return (
		<div>
			<p>Hello World!</p>
		</div>
	);
}

// 他のjavascriptからimportして利用できるようにするため、exportする
export default App;