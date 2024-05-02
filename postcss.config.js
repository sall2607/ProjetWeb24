const purgecc = require('@fullhuman/postcss-purgecss')
const autoprefixer = require('autoprefixer')
const postcssCustomProperties = require('postcss-custom-properties')
const postcssNested = require('postcss-nested')


module.exports = {
    plugins: [
        postcssCustomProperties,
        postcssNested,
        autoprefixer,
        purgecss({
            content: [ 
                './index.html',               
                './assets/**/*.vue',
                './assets/**/*.js',
                './assets/**/*.jsx',
                './assets/**/*.ts',
                './assets/**/*.tsx',
                './assets/**/*.css',
                './assets/**/*.scss',
                './assets/**/*.sass',
                
            ],
            defaultExtractor: content => content.match(/[\w-/:]+(?<!:)/g) || [],
            whitelist: ['html', 'body', 'nuxt-progress', 'nuxt-link', 'nuxt-button', 'nuxt-icon', 'nuxt-svg', 'nuxt-img', 'nuxt-img-lazy', 'nuxt-img-placeholder', 'nuxt-img-placeholder-lazy', 'nuxt-img-placeholder-fade', 'nuxt-img-placeholder-fade-lazy', 'nuxt-img-placeholder-blur', 'nuxt-img-placeholder-blur-lazy', 'nuxt-img-placeholder-blur-fade', 'nuxt-img-placeholder-blur-fade-lazy', 'nuxt-img-placeholder-blur-blur', 'nuxt-img-placeholder-blur-blur-lazy', 'nuxt-img-placeholder-blur-blur-fade', 'nuxt-img-placeholder-blur-blur-fade-lazy', 'nuxt-img-placeholder-blur-blur-blur-fade', 'nuxt-img-placeholder-blur-blur-blur-fade-lazy', 'nuxt-img-placeholder-blur-blur-blur-blur-fade-lazy', 'nuxt-img-placeholder-blur-blur-blur-blur-blur-fade-lazy', 'nuxt-img-placeholder-blur-blur-blur-blur-blur-blur-fade-lazy', 'nuxt-img-placeholder-blur-blur-blur-blur-blur-blur-blur-fade-lazy', 'nuxt-img-placeholder-blur-blur-blur-blur-blur-blur-blur-blur-fade-lazy', 'nuxt-img-placeholder-blur-blur-blur-blur-blur-blur-blur-blur-blur-fade-lazy', 'nuxt-img-placeholder-blur

            ],
            keyframes: true,
            fontFace: true,
            rejected: true,
            whitelistPatterns: [/^nuxt-/],
            whitelistPatternsChildren: [/^nuxt-/],
            extensions: ['js', 'vue', 'ts', 'tsx', 'css', 'scss', 'sass'],
            extractors: [
                {
                    extractor: content => content.match(/[\w-/:]+(?<!:)/g) || [],
                    extensions: ['js', 'vue', 'ts', 'tsx', 'css', 'scss', 'sass']
                }
            ]
        })
    ]
}

