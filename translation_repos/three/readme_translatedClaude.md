# three.js
[![NPM Package][npm]][npm-url]
[![Build Size][build-size]][build-size-url]
[![NPM Downloads][npm-downloads]][npmtrends-url]
[![DeepScan][deepscan]][deepscan-url]
[![Discord][discord]][discord-url]

#### JavaScript 3D Bibliothek

Das Ziel des Projekts ist es, eine benutzerfreundliche, leichtgewichtige, browserübergreifende und universell einsetzbare 3D-Bibliothek zu erstellen. Die aktuellen Builds enthalten nur WebGL- und WebGPU-Renderer, aber SVG- und CSS3D-Renderer sind auch als Addons verfügbar.

[Beispiele](https://threejs.org/examples/) &mdash;
[Dokumentation](https://threejs.org/docs/) &mdash;
[Handbuch](https://threejs.org/manual/) &mdash;
[Wiki](https://github.com/mrdoob/three.js/wiki) &mdash;
[Migration](https://github.com/mrdoob/three.js/wiki/Migration-Guide) &mdash;
[Fragen](https://stackoverflow.com/questions/tagged/three.js) &mdash;
[Forum](https://discourse.threejs.org/) &mdash;
[Discord](https://discord.gg/56GBJwAnUS)

### Verwendung

Dieser Code erstellt eine Szene, eine Kamera und einen geometrischen Würfel und fügt den Würfel zur Szene hinzu. Anschließend wird ein `WebGL`-Renderer für die Szene und Kamera erstellt und dieser Viewport zum `document.body`-Element hinzugefügt. Schließlich wird der Würfel innerhalb der Szene für die Kamera animiert.

```javascript
import * as THREE from 'three';
const width = window.innerWidth, height = window.innerHeight;
// init
const camera = new THREE.PerspectiveCamera( 70, width / height, 0.01, 10 );
camera.position.z = 1;
const scene = new THREE.Scene();
const geometry = new THREE.BoxGeometry( 0.2, 0.2, 0.2 );
const material = new THREE.MeshNormalMaterial();
const mesh = new THREE.Mesh( geometry, material );
scene.add( mesh );
const renderer = new THREE.WebGLRenderer( { antialias: true } );
renderer.setSize( width, height );
renderer.setAnimationLoop( animate );
document.body.appendChild( renderer.domElement );
// animation
function animate( time ) {
	mesh.rotation.x = time / 2000;
	mesh.rotation.y = time / 1000;
	renderer.render( scene, camera );
}
```

Wenn alles gut läuft, sollten Sie [dies](https://jsfiddle.net/v98k6oze/) sehen.

### Klonen dieses Repositories

Das Klonen des Repositories mit seiner gesamten Historie führt zu einem Download von ~2 GB. Wenn Sie nicht die gesamte Historie benötigen, können Sie den `depth`-Parameter verwenden, um die Download-Größe erheblich zu reduzieren.

```sh
git clone --depth=1 https://github.com/mrdoob/three.js.git
```

### Änderungsprotokoll

[Veröffentlichungen](https://github.com/mrdoob/three.js/releases)

[npm]: https://img.shields.io/npm/v/three
[npm-url]: https://www.npmjs.com/package/three
[build-size]: https://badgen.net/bundlephobia/minzip/three
[build-size-url]: https://bundlephobia.com/result?p=three
[npm-downloads]: https://img.shields.io/npm/dw/three
[npmtrends-url]: https://www.npmtrends.com/three
[deepscan]: https://deepscan.io/api/teams/16600/projects/19901/branches/525701/badge/grade.svg
[deepscan-url]: https://deepscan.io/dashboard#view=project&tid=16600&pid=19901&bid=525701
[discord]: https://img.shields.io/discord/685241246557667386
[discord-url]: https://discord.gg/56GBJwAnUS