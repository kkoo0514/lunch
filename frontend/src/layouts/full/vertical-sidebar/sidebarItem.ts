import {
    AlertCircleIcon,
    ApertureIcon,
    AppsIcon,
    AppWindowIcon,
    BasketIcon,
    BorderAllIcon,
    BorderHorizontalIcon,
    BorderInnerIcon,
    BorderStyle2Icon,
    BorderTopIcon,
    BorderVerticalIcon,
    BoxAlignBottomIcon,
    BoxAlignLeftIcon,
    BoxIcon,
    BoxModelIcon,
    BrandTidalIcon,
    CalendarIcon,
    ChartArcsIcon,
    ChartAreaIcon,
    ChartCandleIcon,
    ChartDonut3Icon,
    ChartDotsIcon,
    ChartLineIcon,
    ChartRadarIcon,
    ColumnsIcon,
    CopyIcon,
    CurrencyDollarIcon,
    EditIcon,
    EyeTableIcon,
    FileCheckIcon,
    FileDotsIcon,
    FilesIcon,
    FileTextIcon,
    FilterIcon,
    HelpIcon,
    JumpRopeIcon,
    LayoutDashboardIcon,
    LayoutKanbanIcon,
    LoginIcon,
    MailIcon,
    Message2Icon,
    MoodHappyIcon,
    PageBreakIcon,
    PhotoAiIcon,
    PointIcon,
    RotateIcon,
    RowInsertBottomIcon,
    SearchIcon,
    ServerIcon,
    SettingsIcon,
    ShoppingCartIcon,
    SocialIcon,
    SortAscendingIcon,
    TicketIcon,
    TypographyIcon,
    UserCircleIcon,
    UserPlusIcon,
    UserShieldIcon,
    ZoomCodeIcon
} from 'vue-tabler-icons';

export interface menu {
    header?: string;
    title?: string;
    icon?: any;
    to?: string;
    chip?: string;
    chipColor?: string;
    chipBgColor?: string;
    chipVariant?: string;
    chipIcon?: string;
    children?: menu[];
    disabled?: boolean;
    type?: string;
    subCaption?: string;
    external?: boolean;
}

const sidebarItem: menu[] = [
    { header: 'Home' },
    {
        title: 'Dashboard',
        icon: LayoutDashboardIcon,
        to: '/',
        external: false
    },
    { header: 'utilities' },
    {
        title: 'Typography',
        icon: TypographyIcon,
        to: '/ui/typography',
        external: false
    },
    {
        title: 'Shadow',
        icon: CopyIcon,
        to: '/ui/shadow',
        external: false
    },

    { header: 'auth' },
    {
        title: 'Login',
        icon: LoginIcon,
        to: '/auth/login',
        external: false
    },
    {
        title: 'Register',
        icon: UserPlusIcon,
        to: '/auth/register',
        external: false
    },
    { header: 'Extra' },
    {
        title: 'Icons',
        icon: MoodHappyIcon,
        to: '/icons',
        external: false
    },
    {
        title: 'Sample Page',
        icon: ApertureIcon,
        to: '/sample-page',
        external: false
    }
];

export default sidebarItem;
