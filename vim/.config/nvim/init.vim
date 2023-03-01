" Vim-plug and Plugins
call plug#begin(system('echo -n "${XDG_CONFIG_HOME:-$HOME/.config}/nvim/plugged"'))
Plug 'sainnhe/sonokai'
Plug 'vim-airline/vim-airline'
Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}
Plug 'nvim-tree/nvim-web-devicons'
Plug 'nvim-tree/nvim-tree.lua'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'godlygeek/tabular'
Plug 'preservim/vim-markdown'
Plug 'ellisonleao/glow.nvim'
Plug 'preservim/vim-pencil'
call plug#end()

" Colorscheme
let g:airline_theme = 'sonokai'
let g:airline_powerline_fonts = 1
let g:sonokai_transparent_background = 1
colorscheme sonokai


" Keybindings
nnoremap <A-d> :NvimTreeToggle<CR>
nnoremap <A-D> :NvimTreeFocus<CR>
nnoremap <A-c> :NvimTreeFindFile<CR>
nnoremap <A-C> :NvimTreeCollapseKeepBuffers<CR>
nmap <silent> gd <Plug>(coc-definition)
nmap <silent> gy <Plug>(coc-type-definition)
nmap <silent> gi <Plug>(coc-implementation)
nmap <silent> gr <Plug>(coc-references)

    """ Use TAB to trigger completion and navigate, S-Tab to deselect completion
function! CheckBackspace() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~# '\s'
endfunction
inoremap <silent><expr> <TAB>
      \ coc#pum#visible() ? coc#pum#next(1) :
      \ CheckBackspace() ? "\<Tab>" :
      \ coc#refresh()
inoremap <expr><S-TAB> coc#pum#visible() ? coc#pum#prev(1) : "\<C-h>"

    """ Use <CR> to accept proposed completion
inoremap <silent><expr> <CR> coc#pum#visible() ? coc#pum#confirm()
                              \: "\<C-g>u\<CR>\<c-r>=coc#on_enter()\<CR>"

" Basics
set nu
set tabstop=4
set shiftwidth=4
set expandtab
set clipboard+=unnamedplus

" COC Config
let g:coc_global_extensions = ['coc-pairs', 'coc-pyright', 'coc-rust-analyzer', 'coc-html', 'coc-css', 'coc-tsserver']

" Tree-Sitter Lua Config
lua << EOF
require'nvim-treesitter.configs'.setup {

  ensure_installed = { "c", "rust", "python", "html", "css", "javascript"},
  sync_install = false,
  auto_install = true,

  highlight = {
    enable = true,

    -- Disable highlighting for large files to avoid slowing down
    disable = function(lang, buf)
        local max_filesize = 100 * 1024 -- 100 KB
        local ok, stats = pcall(vim.loop.fs_stat, vim.api.nvim_buf_get_name(buf))
        if ok and stats and stats.size > max_filesize then
            return true
        end
    end,

    additional_vim_regex_highlighting = false,
  },
  require("nvim-tree").setup(),

}
require('glow').setup({style = "dark", width=120})
EOF
