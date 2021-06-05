// Reactを利用する場合、必ずreactをインポートする必要がある
import React from 'react';
// HTML要素にAppコンポーネントを描画する場合、react-domも必要になる
// 今回は、Appコンポーネントを<div id="root"></dic>に描画するため、react-domも
import ReactDom from 'react-dom';
// Appコンポーネントをインポートする
import App from './App';

// Appコンポーネントを<div id="root"></div>に描画する。
// /src/index.jsなどがビルドされたjavascriptファイルはpublic/index.htmlで読み込まれる
// そのため、public/index.htmlの<div id="root"></div>にAppコンポーネントが描画される
ReactDom.render(
	<React.StrictMode>
		<App/>
	</React.StrictMode>,
	document.getElementById('root')
);